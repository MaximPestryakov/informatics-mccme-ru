import * as _ from 'lodash';

import axios from '../utils/axios';


export function fetchStatement(statementId) {
  return (dispatch) => {
    const url = `/statement/${statementId}`;
    return dispatch({
      type: 'GET_STATEMENT',
      payload: axios.get(url),
      meta: {
        statementId,
      },
    });
  };
}


export function setSettings(statementId, settings) {
  return (dispatch) => {
    const url = `/statement/${statementId}/set_settings`;
    return dispatch({
      type: 'POST_STATEMENT_SET_SETTINGS',
      payload: axios.post(
        url,
        settings,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      ),
      meta: {
        statementId,
      },
    });
  };
}


export function start(statementId, virtual = false) {
  return (dispatch) => {
    const url = `/statement/${statementId}/start${virtual ? '_virtual' : ''}`;
    return dispatch({
      type: `POST_STATEMENT_START${virtual ? '_VIRTUAL' : ''}`,
      payload: axios.post(url),
      meta: { statementId },
    }).then(() => dispatch(fetchStatement(statementId)));
  };
}


export function finish(statementId, virtual = false) {
  return (dispatch) => {
    const url = `/statement/${statementId}/finish${virtual ? '_virtual' : ''}`;
    return dispatch({
      type: `POST_STATEMENT_FINISH${virtual ? '_VIRTUAL' : ''}`,
      payload: axios.post(url),
      meta: { statementId },
    }).then(() => dispatch(fetchStatement(statementId)));
  };
}