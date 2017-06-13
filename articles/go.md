﻿#Go
Сегодня на [informatics.mccme.ru](http://informatics.mccme.ru) появилась возможность сдавать решения на еще одном замечательном языке программирования. На языке **GO**. 
Этот язык был разработан компанией Google и имеет открытый исходный код.

Основной целью, при его создании, ставилось сделать простой для написания и понимания (как, например, python), и в то же время быстрый язык.
Go используется во множестве компаний, например: Google, Dropbox, SoundCloud и многих других. 
Все больше и больше программистов, занимающихся, например, web разработкой, отбрасывают старые языки (например PHP) и переходят на Go. Почему бы и вам не попробовать писать на нем?
###Hello, world!

Начать изучение языка GO стоит с программы "Hello, world!". So, let's GO.

Для начала нам потребуется его скачать: [golang.org](https://golang.org)

После установки, время писать код!

```go
package main //Название "package". Если мы пишем программу из одного файла, то это ни на что не влияет, но если бы наша программа содержала много отдельных файлов(модулей), то название стоило бы сделать чуть более информативным, чем main. 

import "fmt" //Подключаем встроенный модуль fmt, в котором лежит в том числе функция Println.

func main() { //Объявляем функцию main - функцию, которая первой запустится при запуске нашей программы.
    fmt.Println("hello world") // Вызываем функцию, которая печатает строку
}
```

Теперь, чтобы запустить программу пишем в консоли, находясь в той же папке, что и наш файл: 
```
go build hello_world.go
hello_world.exe
```

Или же вы можете использовать какую-либо среду разработки, если вам не нравится компилировать из консоли. Например, для eclipse есть неплохой плагин для работы с Go: https://github.com/GoClipse/goclipse
###Переменные и константы
Переменные в Go нужно объявлять. Есть несколько способов.

```go
a := 1 // оператор := означает, что мы создаем переменную такого же типа, что и значение справа от него и сразу присваиваем его этой переменной.
var b, c int // Создаем 2 неинициализированных переменных типа int
```


Изменить тип переменной в языке Go нельзя. Решили int, значит int. Например, следующий код выдаст ошибку компиляции:
```go
a := 1
a := "Go is nice"
```

Можно создавать константы, например
```go
const n = 5000
```

###Массивы и циклы
Давайте попробуем написать какую-нибудь программу с массивами.

```go
package main
import "fmt"
func main() {
    var n int // Объявим переменную типа int
    fmt.Scanf("%d", &n) // Считаем ее значение аналогом scanf языка C++.
    a := make([]int, n); //Создадим slice типа int из n элементов (аналог обычных массивов, имеющий некоторой дополнительный функционал)
    for i := 0; i < n; i++ { // Можно писать цикл for в форме, привычной для тех, кто писал до этого на C подобных языках. 
        fmt.Scanf("%d", &a[i]); //Напоминаю, что & перед переменной обозначает, что в функцию мы передаем ссылку на эту переменную, а не значение.
    }
    sum := 0 //Создаем переменную sum, тип которой автоматически устанавливается по присываемому значению.
    for _,x := range a { //Еще один способ написания цикла for. В данном случае range a будет "возвращать" 2 элемента - индекс и значение в массиве(так же, как и в питоне, Go умеет делать "множественные" присваивания. Так как индекс нам в данном случае не нужен, то ничему не будем его присваивать - присвоим его _. (Так сказать, присваивание вникуда), а значение элемента массива присвоим переменной x. Range так же можно использовать для того, чтобы пробегаться по всем элементам map и других структур.  
        sum += x
    }
    fmt.Printf("%d\n", sum)
}
```
###Сортировка
Настало время написать сортировку. Куда же без нее. 

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []int{5, 2, 6, 3, 1, 4} // Создаем "slice" с заданными значениями.
	sort.Ints(s) // Вызываем функцию, сортирующую "slice" из элементов типа int.
	fmt.Println(s) 
}
```

Кстати, в языке Go нет ключевой команды while. Вместо него используется все тот же for.
Например,

```go
a := 1
for a < 129 {
	a *= 2
}
```


А еще язык Go не даст вам скомпилировать программу, если в ней есть неиспользуемые переменные или "package". Учитесь подключать и создавать только то, что нужно.

###Условный оператор
Оператор if в языке go практически ничем не отличается от аналогов в других языках, кроме маленького дополнения. В нем можно делать "инициализирующее присваивание", как в цикле for языка C.
```go 
var a int
fmt.Scanf("%d", &a)
if a > 0 {
	fmt.Println("Bigger then Zero")
} else {
	fmt.Println("Smaller then Zero")
}
var a1, a2, a3, a4 int
if a, _ := fmt.Scanf("%d%d%d%d", &a1, &a2, &a3, &a4); a < 4 {  //Создается локальная переменная, которая будет доступна только в теле условного оператора. 
{
 fmt.Printf("Only %d variables were readed =(", a);
}
```

###Map
Также в языке Go есть такая замечательная вещь, как map. По сути это "ассоциативный массив". Если вы пишете не на pascal, то с ее аналогом вы, скорее всего, много раз сталкивались. 
Пример использования map:
```go
m := make(map[string]int) //Создаем map с типом ключей string и значениями типа int
m["Misha"] = 100 
m["Petya"] = 200
value, existance := m["Misha"] //Обращение к map возвращает 2 значения. Значение элемента и булевскую переменную - "существует ли элемент".

if existance {
    fmt.Println("Key Misha exist in Map")
    fmt.Printf("Misha's value is %d\n", value);
    fmt.Printf("Misha's value again is %d\n", m["Misha"])
}
delete(m, "Misha")

_, existance = m["Misha"]

if !existance {
    fmt.Println("No Misha any more")
}
```

###Точки с запятой

Вы могли заметить, что я еще ни разу не писал ; в коде. 
На самом деле, они используются, но их "дописывает" предпроцессор перед компиляцией. Не нужно их использовать лишний раз. Это не "true Go way". 
Для "дописывания" препроцессор использует простое правило, которое по человечески можно сформулировать так:
"Препроцессор всегда вставляет точку с запятой перед концом строки если на этой строке может заканчиваться оператор (будь то присваивание, вызов функции или что угодно).

Для тех, кто любит более строгие определения существует описание из документации, которое не так уж и легко перевести на русский:

>The rule is this. If the last token before a newline is an identifier (which includes words like int and float64), a basic literal such as a number or string constant, or one of the tokens
>
>break continue fallthrough return ++ -- ) }
>the lexer always inserts a semicolon after the token. 


###Функции
В объявлении функции нет ничего сложного.
```go
func plus(int a, int b)int  { // тип указывается в конце функции, в отличие о C. 
    return a + b // Возвращает значение a + b и выходит их функции. 
}
```
А можно возвращать сразу много значений, например:
```go
func many(a, b int)(int, int) { // Можно писать через запятую несколько переменных одного типа, чтобы не повторяться лишний раз. В скобках перечисляем типы переменных, которые планируем возвращать.
    return a + b, a * b
}

a, b := many(1, 2)
fmt.Printf("%d %d\n", a, b);
```

###Большие числа
Как в любом современном языке программирования, в Go присутствует встроенная длинная арифметика. 
Давайте напишем программу, которая найдет первое число Фиббоначи с как минимум 100 цифрами.

```go
package main
import (
	"fmt"
	"math/big"
)

func main() {
	a := big.NewInt(0)
	b := big.NewInt(1)

	var limit big.Int // Создаем переменную типа big.Int
	limit.Exp(big.NewInt(10), big.NewInt(99), nil) // Присваиваем ей значение 10 ^ 99

	for a.Cmp(&limit) < 0 { // Идем циклом, пока текущее число меньше 10^99
		a.Add(a, b)
		a, b = b, a
		//Находим следующее число Фиббоначи
	}
	fmt.Println(a)
	
	//Вероятностная проверка числа на простоту. Работает очень быстро, по сравнению со стандартным алгоритмом за sqrt(N). Параметр - количество "раундов", на которых будет тестироваться число. Чем больше раундов, тем медленнее, но точнее.
	fmt.Println(a.ProbablyPrime(20))

}
```
###Реальная задача
Для примера, можно рассмотреть самую простую задачу с финального тура заочной олимпиады школьников про программированию. 
Суть задачи заключалась в том, чтобы среди n точек найти количество таких пар, что манхэтанское растояние между ними было равно евклидовому.
На питоне на туре эту задачу на полный бал удалось сдать лишь одному человеку, который использовал PyPy и еще как-то жутко оптимизировал память. Авторское решение задачи на Java работает на максимальном тесте за 1.2 секунды, данное же решение на Go работает всего 0.23 секунды, лишь на 0.06 секунд отставая от решения на С++.
```go
package main

import (
	"bufio"
	"fmt"
	"os"
)
//Один из вариантов написания быстрого считывания чисел.
//Можно просто запомнить или каждый раз копировать.
var in = bufio.NewScanner(os.Stdin)
func readInt64() int64 {
	if !in.Scan() {
		panic(in.Err())
	}
	res := int64(0)
	for _, b := range in.Bytes() {
		res = res*10 + int64(b-'0')
	}
	return res
}

func main() {
	in.Split(bufio.ScanWords)

	n := readInt64()
    xm := make(map[int64]int64)
    ym := make(map[int64]int64)
    xym := make(map[int64]int64)
    INF := int64(1e9)
    for i:= int64(1); i <= n; i++ {
        x, y := readInt64(), readInt64()
        xm[x] += 1
        ym[y] += 1
        xym[(x + INF) * INF + y] += 1
    }
    ans := int64(0)
    for _, v := range xm {
        ans += v * (v - 1) / 2
    }
    for _, v := range ym {
        ans += v * (v - 1) / 2
    }
    for _, v := range xym {
        ans -= v * (v - 1) / 2
    }
    fmt.Println(ans);
}
```
Решение написано максимально неоптимально(map вместо сортировки, int64 вместо int и т.д) и все равно работает практически моментально.



###Заключение
Нельзя описать все возможности, которые предоставляет язык Go. Их слишком много. Я обязательно советую попробовать вам писать на нем. Он является очень простым и удобным в использовании. Компилируемость добавляет ему скорости и надежности (да, да, у меня тоже падал код на питоне с runtime на тесте 84, потому что я в одном месте опечатался в названии функции). Его простота позволяет писать код куда быстрее, чем на таких языках, как C++ и Java. 
Для начала советую попробовать порешать задачи, которые можно найти в разделе: Изучение языка программирования, и лишь, когда Вы начнете уверенно писать на нем, приступать к более олимпиадным задачам.

К Вам всегда придерались учителя? Говорили, что ваш код некрасиво отформатирован? Команда gofmt. И никаких вопросов. Она, вы не поверите, форматирует код на языке go согласно принятому стандарту.


###Полезные ссылки:
https://gobyexample.com/ - куча всего, что есть в языке Go с примерами. 
https://golang.org/pkg/ - документация стандартной библиотеки с примерами. Так же там можно посмотреть исходный код, библиотек. Например, я никогда до этого не видел, как пишется функция sqrt - https://golang.org/src/math/sqrt.go
Ну и основные ресурсы в изучении любого нового языка программирования:
google.com и yandex.ru