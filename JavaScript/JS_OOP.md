JS : 함수형 언어로 처음 개발. 프로토타입을 이용해 객체 지향 요소 도입.
<br>


# 프로토타입과 클래스

#### 다른 언어의 객체 지향

- B가 A를 상속받는다 → B 안에 A가 있다. (B에서 A의 대상을 찾을 수 있다.)

#### 자바스크립트의 객체지향

- B가 A를 상속받는다 → B는 A를 가리킨다. (연결 관계. B에서 대상을 찾아서 없으면 가리키고 있는 A에서 찾는다.)

**“A는 B의 프로토타입이다.”**

```jsx
let cat = {
	name: '고양이',
	age: 5,

	// ===================== 메서드 넣어줘!

	attack: function() {
		console.log(`${this.name} 냥냥펀치`)
	}
}

console.log(cat.name)    // 고양이
console.log(typeof cat)  // object
cat.attack()             // 고양이 냥냥펀치

let munchkin = {
	name: '키티',
	age: 2
}

// ===================== 상속 기능 넣어줘!

munchkin.__proto__ = cat
munchkin.attack()        // 키티 냥냥펀치

// ===================== new 키워드 넣어줘!

function Cat(name, age) {
	this.name = name
	this.age = age
}

// 프로토타입이라는 공간에 attack 메서드 써놓기

Cat.prototype.attack = function () {
	console.log(`${this.name} 냥냥펀치`)
}
let myCat = new Cat('키티', 3)
myCat.attack()           // 키티 냥냥펀치

// ===================== class 넣어줘!

class Cat {
	constructor(name, age) {
		this.name = name
		this.age = age
	}
}

Cat.prototype.attack = function() {
	console.log(`${this.name} 냥냥펀치`)
}

let myCat = new Cat('키티', 3)
myCat.attack()           // 키티 냥냥펀치
```

- JS는 객체지향 언어다.
- JS는 class가 있지만 내부적으로는 function(+프로토타입)을 사용하고 있다.

<br>

---

# this

```jsx
const myPrice = {
	exchangeRate: 1432,
	prices: [10, 50, 100],
	
	printPrice: function() {
		this.prices.forEach(function(price) {
			console.log(price * this.exchangeRate)  // this : window. NaN 값이 뜸
		}
	}
}

// ======================= bind 이용

const myPrice = {
	exchangeRate: 1432,
	prices: [10, 50, 100],
	
	printPrice: function() {
		this.prices.forEach(function(price) {
			console.log(price * this.exchangeRate)  // this : myPrice. 제대로 계산됨.
		}.bind(this)                              // bind : 상위 객체의 this로 bind 해줌
	}
}
myPrice.printPrices()  // 14320, 71600, 143200

// ======================= arrow 함수 이용 (bind 내포)

const myPrice = {
	exchangeRate: 1432,
	prices: [10, 50, 100],
	
	printPrice: function() {
		this.prices.forEach((price) => {
			console.log(price * this.exchangeRate)  // this : myPrice. 제대로 계산됨.
		}
	}
}
myPrice.printPrices()  // 14320, 71600, 143200
```
<br>

<aside>
⭐ Callback 함수는 인자로 들어가는 함수다.

</aside>

<aside>
⭐ Callback 함수(arrow function)는 한단계 상위 객체의 this를 가리킨다.

</aside>
<br>


```jsx
const obj = {
    a: 1,

    test1: function() {
      console.log(this.a)
    },

    test2: () => {
      console.log(this.a)
    },
  }

  obj.test1() // 1
  obj.test2() // undefined

myFunc = function() {
	console.log(this.a)
}

const a = 1
const obj = {
	a: 2,
	print: function(func) {
		func()
	}
}
obj.print(myFunc) // undefined
```