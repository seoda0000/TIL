import { useState, useEffect } from "react";
import MeetupList from "../components/meetups/MeetupList";

function AllMeetupsPage() {
  const [isLoading, setIsLoading] = useState(true);
  const [loadedMeetups, setLoadedMeetups] = useState([]);

  // useEffect
  // 특정 조건에서만 함수가 실행되도록 함. 배열 안의 값이 변화할 때마다 실행. 부수효과 (화면에 표시되는 것들에 직접적으로 영향을 미치지 않는 요소)를 제어할 때 쓰임.
  // 첫번째 인자 : 함수
  // 두번째 인자 : 생략 시 컴포넌트 함수가 실행될 때마다 실행됨. (의미 없음)
  // 두번째 인자가 추가되면 배열 값을 effect가 마지막으로 실행되었을 때의 값과 비교해서 변화하였을 때 실행. 빈 배열이면 의존성이 없음 -> 처음 랜더링 될 때만 실행.
  // 만약 외부에서 데이터를 참조한다면 (props 사용) 두번째 인자에 추가해야 함.

  useEffect(() => {
    setIsLoading(true);
    fetch(
      "https://react-getting-start-b30e9-default-rtdb.firebaseio.com/meetups.json"
    )
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        const meetups = [];
        for (const key in data) {
          const meetup = {
            id: key,
            ...data[key], // 객체에 데이터 키를 분배
          };
          console.log(meetup);
          meetups.push(meetup);
        }
        setIsLoading(false);
        setLoadedMeetups(meetups); // 외부 의존성을 갖고 있으나, state update 함수는 절대 바뀌지 않는다. 매번 같은 작업을 수행한다. 따라서 두번째 인자에 추가하지 않아도 됨.
      });
  }, []); // 외부 의존성이 없으므로 빈 배열.

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
    );
  }

  return (
    <section>
      <h1>All Meetups Page</h1>
      <MeetupList meetups={loadedMeetups} />
    </section>
  );
}

export default AllMeetupsPage;
