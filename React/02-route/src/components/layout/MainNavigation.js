import { Link } from "react-router-dom";

// CSS 모듈 : module.css로 끝나야함
import classes from "./MainNavigation.module.css";
// 모든 css가 자바스크립트 객체(classes)의 속성이 된다.

function MainNavigation() {
  return (
    <header className={classes.header}>
      <div className={classes.logo}>React Meetups</div>
      <nav>
        <ul>
          <li>
            <Link to="/">All Meetups</Link>
          </li>
          <li>
            <Link to="/new-meetup">Add New Meetups</Link>
          </li>
          <li>
            <Link to="/favorite">My Favorite</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
