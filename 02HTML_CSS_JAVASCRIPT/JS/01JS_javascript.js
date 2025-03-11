
//웹브라우저 콘솔에 id title을 갖는 태그를 호출 
const title = document.querySelector("#title");
    console.log(title);


// 링크 클릭 이벤트 연결하기
const link = document.querySelector("a")
// link.addEventListener("click", ()=>{
    // console.log("링크를 클릭했습니다.");
// });

// 링크를 클릭해도 링크가 작되지 않고 로그만 찍히도록 
link.addEventListener("click", (e)=>{
    e.preventDefault();
    console.log("링크를 클릭했습니다");
});

// html 요소에 마우스 이벤트 연결하기

const box = document.querySelector("#box");
box.addEventListener("mouseenter", ()=>{
    box.style.backgroundcolor = "hotpink";
});

box.addEventListener("mouseleave", ()=>{
    box.style.backgroundcolor = "aqua";
});

// 반복되는 요소에 이벤트 한꺼번에 연결하기
// 
const list = document.querySelectorAll(".list li");
console.log(list);
// []안에 있는 자료형을 list ALL 함수를 써야 다 들어감

for(let el of list){
    el.addEventListener("click", e=>{
        e.preventDefault(); // 링크는 작동하지 않고
        console.log(e.currentTarget.innerText);
        //innnertext 사용하면 출력 가능
    });
}

//클릭이벤트가 발생할 떄 숫자가 증가하거나 감소

const btnPlus = document.querySelector(".btnPlus");
const btnMinus = document.querySelector(".btnMinus");

let num = 0; //제어할 숫자값을 0으로 초기화

//bntPlus를 클릭할때 
btnPlus.addEventListener("click", e=>{
    e.preventDefault();
    num++; // num 값을 1 씩 증가
    console.log(num);

});

// btnMinus 클릭할 떄
btnMinus.addEventListener("click", e=>{
    e.preventDefault(); // 링크는 작동하지 않고
    num--; // num 값을 1 씩 감소
    console.log(num);

});

//버튼을 클릭하면 좌우로 회전하는 박스 만들기

const btnLeft = document.querySelector(".btnLeft");
const btnRight = document.querySelector(".btnRight");
const box2 = document.querySelector("#box2");
const deg = 45; //회전할 각도
let num2 = 0; //증가시킬 값을 0으로 초기화

// btnLeft를 클릭할때 
btnLeft.addEventListener("click", e=>{
    e.preventDefault();
    num2--;
    console.log(`num2: ${num2}`);
    // 문자열과 변수 값을 같이 써줄 때 ``를 같이 써줌 (JS에서만 씀)
    box2.style.transform = `rotate(${num2 * deg}deg)`;
});

// btnRight를 클릭할때 
btnRight.addEventListener("click", e=>
    //원래 funtion(e0) 함수였는데 바뀌었음
    {
    e.preventDefault();
    num2++;
    console.log(`btnRight를 클릭했을 때 num2에 있는 값: ${num2}`);
    // console.log(num2); 변수만 찍는 함수
    // 문자열과 변수 값을 같이 써줄 때 ``를 같이 써줌
    //``를 안써주면 변수 안에 있는 값이 안나옴
    // 출력값 뿐만 아니라 무조건 ``을 같이 써줌
    box2.style.transform = `rotate(${num2 * deg}deg)`;
});

