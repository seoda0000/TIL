import { createContext, useState } from "react";

const FavoritesContext = createContext({
  favorites: [],
  totalFavorites: 0,
  addFavorite: (favoriteMeetup) => {},
  removeFavorite: (meetupId) => {},
  itemIsFavorite: (meetupId) => {},
}); // Context : 자바 스크립트 객체

export function FavoritesContextProvider(props) {
  // 역할 : 값을 받으려하는 컴포넌트에 Context 제공 / Context 업데이트
  const [userFavorites, setUserFavorites] = useState([]);

  // 함수를 통해 Context를 관리할 수 있다.

  function addFavoriteHandler(favoriteMeetup) {
    setUserFavorites((prevUserFavorites) => {
      return prevUserFavorites.concat(favoriteMeetup);
    });
    // concat : 새 요소가 추가된 배열 반환
    // 바로 변화를 state에 반영하기 위해 함수를 이용
  }

  function removeFavoriteHandler(meetupId) {
    setUserFavorites((prevUserFavorites) => {
      return prevUserFavorites.filter((meetup) => meetup.id !== meetupId);
    });
  }

  function itemIsFavoriteHandler(meetupId) {
    return userFavorites.some((meetup) => meetup.id === meetupId);
  }

  const context = {
    favorites: userFavorites,
    totalFavorites: userFavorites.length,
    addFavorite: addFavoriteHandler,
    removeFavorite: removeFavoriteHandler,
    itemIsFavorite: itemIsFavoriteHandler,
  };

  return (
    // Provider : Context와 상호작용하는 모든 컴포넌트를 감싸야 한다.
    <FavoritesContext.Provider value={context}>
      {props.children}
    </FavoritesContext.Provider>
  );
}

export default FavoritesContext;
