// Primitives: number, string, boolean
// More complex types: arrays, objects
// Function types, parameters

// ==========
// Primitives
// ==========

let age: number; // 소문자로 시작해야 한다. 대문자면 js type임.
age = 12.1;

let age2: number = 12; // 선언과 할당 동시에 가능

let userName: string;
userName = "Max";

let isInstructor: boolean;
isInstructor = true;

// ==================
// More complex types
// ==================

let hobbies: string[]; // 문자열 배열

hobbies = ["Sports", "Cooking"];

let p; // type: 지정하지 않으면 any

let person: {
  // 객체 타입 지정
  name: string;
  age: number;
};

person = {
  name: "Max",
  age: 32,
};

// person = {
//   isEmployee: true, // error
// };

let people: {
  // 객체 배열 타입 지정
  name: string;
  age: number;
}[];

// ★★★
// Type inference
// 명시적인 선언이 없어도 ts는 가능한 많은 타입을 유추하려고 한다.

let course = "React - The Complete Guide"; // type이 string으로 자동 지정

// course = 12341; // error

// ★★★
// 다중(union) 유형 선언하기

let course2: string | number | boolean = "React - The Complete Guide"; // type이 string으로 자동 지정

course2 = 12341;

let userName2: string | string[];

// ★★★
// Type Allias
// 타입 별칭을 이용해서 재사용
// type 타입 이름 = 타입

type Student = {
  name: string;
  score: number;
};

let students: Student[];

// ================
// Function & types
// ================

function goAdd(a: number, b: number) {
  return a + b; // 타입 추론됨
}

function goAdd2(a: number, b: number): number | string {
  return a + b; // 타입 선언도 가능
}

function printOutput(value: any) {
  console.log(value);
} // return이 없을 때 void return type을 갖는다 -> undefined

// ★★★
// Generics

// 문제 상황
// 타입 유연성을 구현하면 안전성을 확보하지 못한다.

function insertAtBeginning(array: any[], value: any) {
  const newArray = [value, ...array];
  return newArray;
}

const demoArray = [1, 2, 3];
const updatedArray = insertAtBeginning(demoArray, -1); // [-1, 1, 2, 3] : any array

updatedArray[0].split(""); // any로 선언해서 코드상에서는 에러가 뜨지 않지만, 실행하면 에러가 뜸.

// 해결 방법 : Generic
// 타입 유연성과 안정성을 동시에 확보하는 방법.

function insertAtBeginning2<T>(array: T[], value: T) {
  // Generic 타입 선언으로 ts가 값을 탐색한다.
  const newArray = [value, ...array];
  return newArray;
}

const demoArray2 = [1, 2, 3];

const updatedArray2 = insertAtBeginning2(demoArray2, -1); // [-1, 1, 2, 3]: number array

const stringArray = insertAtBeginning2(["a", "b", "c"], "d"); // ['d', 'a', 'b', 'c']: string array

// updatedArray2[0].split(""); // ts가 에러를 인식함.

// Generic으로 이용하여 Array를 표현할 수 있다.

let nums1: number[] = [1, 2, 3];
let nums2: Array<number> = [1, 2, 3];
