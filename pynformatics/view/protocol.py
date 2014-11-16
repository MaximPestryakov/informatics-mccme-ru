import sys, traceback
import time
import json
import transaction
import zipfile
from xml.etree.ElementTree import ElementTree
from collections import OrderedDict
from pyramid.view import view_config
from pynformatics.model import User, EjudgeContest, Run, Comment, EjudgeProblem, Problem, Statement
from pynformatics.contest.ejudge.serve_internal import EjudgeContestCfg
from pynformatics.view.utils import *
from phpserialize import *
from pynformatics.view.utils import *
from pynformatics.models import DBSession
from pynformatics.models import DBSession
from pynformatics.model.run import to32


@view_config(route_name='protocol.get', renderer='json')
def get_protocol(request):
    try:
        contest_id = int(request.matchdict['contest_id'])
        run_id = int(request.matchdict['run_id'])
        run = Run.get_by(run_id = run_id, contest_id = contest_id)
        try:
            run.tested_protocol
            if (run.user.statement.filter(Statement.olympiad == 1).filter(Statement.timestop > time.time()).filter(Statement.timestart < time.time()).count() == 0):
                res = OrderedDict()
                for num in range(1, len(run.tests.keys()) + 1):
                    res[str(num)] = run.tests[str(num)]
                return res
            else:
                try:
                    return [run.tests["1"]]
                except KeyError as e:
                    return {"result" : "error", "message" : e.__str__(), "stack" : traceback.format_exc()}
        except Exception as e:
            return {"result" : "error", "message" : run.compilation_protocol, "error" : e.__str__(), "stack" : traceback.format_exc()}
    except Exception as e: 
        return {"result" : "error", "message" : e.__str__(), "stack" : traceback.format_exc()}


@view_config(route_name="protocol.get_full", renderer='json')
def protocol_get_full(request):
    try:
        contest_id = int(request.matchdict['contest_id'])
        run_id = int(request.matchdict['run_id'])
        run = Run.get_by(run_id = run_id, contest_id = contest_id)
        prob = run.problem
        out_path = "/home/judges/{0:06d}/var/archive/output/{1}/{2}/{3}/{4:06d}.zip".format(
            contest_id, to32(run_id // (32 ** 3) % 32), to32(run_id // (32 ** 2) % 32), to32(run_id // 32 % 32), run_id
        )
        try:
            prot = get_protocol(request)
            if "result" in prot and prot["result"] == "error":
                return prot
            
            out_arch = None
            run.tested_protocol
            
            for test_num in prot:
                judge_info = run.judge_tests_info[test_num]
                if "input" in judge_info:
                    prot[test_num]["input"] = judge_info["input"]
                else:
                    prot[test_num]["input"] = prob.get_test(int(test_num))

                if "correct" in judge_info:
                    prot[test_num]["corr"] = judge_info["correct"]
                else:
                    prot[test_num]["corr"] = prob.get_corr(int(test_num))


                if "checker" in judge_info:
                    prot[test_num]["checker_output"] = judge_info["checker"]
                if "stderr" in judge_info:
                    prot[test_num]["error_output"] = judge_info["stderr"]
                if "output" in judge_info:
                    prot[test_num]["output"] = judge_info["output"]


                for type in [("o", "output"), ("c", "checker_output"), ("e", "error_output")]:
                    file_name = "{0:06d}.{1}".format(int(test_num), type[0])
                    if out_arch is None:
                        try:
                            out_arch = zipfile.ZipFile(out_path, "r")
                            names = set(out_arch.namelist())
                        except:
                            names = {}
                    if file_name not in names or type[1] in prot[test_num]:
                        continue
                    with out_arch.open(file_name, 'r') as f:
                        prot[test_num][type[1]] = f.read(1024).decode("utf-8")
            if out_arch:
                out_arch.close()
            return prot
        except Exception as e:
            return {"result": "error", "content": e.__str__(), "out_path": out_path}
    except Exception as e:
        return {"result": "error", "content": e.__str__()}
