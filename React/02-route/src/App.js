import { Routes } from "react-router-dom";
import { Route } from "react-router-dom";

import AllMeetupsPage from "./pages/AllMeetups";
import NewMeetupsPage from "./pages/NewMeetups";
import FavoitesPage from "./pages/Favorites";
import Layout from "./components/layout/Layout";

function App() {
  // localhost:3000

  return (
    <Layout>
      <Routes>
        <Route path="/" element={<AllMeetupsPage />} />
        <Route path="/new-meetup" element={<NewMeetupsPage />} />
        <Route path="/favorite" element={<FavoitesPage />} />
      </Routes>
    </Layout>
  );
}

export default App;
