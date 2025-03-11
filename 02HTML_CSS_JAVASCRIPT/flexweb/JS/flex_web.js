// 모든 article 요소들을 변수 item에 저장 

const items = document.querySelectorAll("article");
//console.log(items)
const aside = document.querySelector("aside");
//cconsol.log(aside);
const close = aside.querySelector("span");

//items 를 반복문으로 돌리기
for(let el of items) {
    //현재 반복이 돌고 있는 아티클 요소에 마우스 이벤트 
    el.addEventListener("mouseenter",e=>{
        //자식인 비디오요소 재생
        e.currentTarget.querySelector("video").play();
    });
    //현재 반복이 돌고 있는 아티클 요소에 마우스 리브 이벤트 발생시 
    el.addEventListener("mouseleave", e=>{
        //자식인 video요소 일시정지
        e.currentTarget.querySelector("video").pause();

    });

    el.addEventListener("click", e=>{
        //제목과 본문의 내용 그리고 비디오 요소의 src값을 변수에 저장
        let tit = e.currentTarget.querySelector("h2").innerText;
        let txt = e.currentTarget.querySelector("p").innerText;
        let vidSrc = e.currentTarget.querySelector("video").getAttribute("src");
        console.log(`title: ${tit}, p의 내용: ${txt}, video 경로: ${vidSrc}`);

        //aside 요소 안쪽의 컨텐츠에 위에 변수 내용 적용
        aside.querySelector("h1").innerText = tit;
        aside.querySelector("p").innerText = txt;
        aside.querySelector("video").setAttribute("src", vidSrc);

        //aside 요소 안쪽의 동영상을 재상하고 aside 요소에 class=on을 붙여 팝업 패널 활성화
        aside.querySelector("video").play();
        aside.classList.add("on");

    });

    //close 버튼 클릭했을 떄

    close.addEventListener("click", ()=>{
        //aside 요소에 클래스 ON을 제거해 비활성화하고 안쪽의 영상을 재생 일시정시 
        aside.classList.remove("on");
        aside.querySelector("video").pause();
    })



}