import { Routes, Route } from "react-router-dom";
import SignUp from "./Signin";
import Login from "./Login";
import Home from "./Home";
export default function App() {
  return (
    <div>
      <Routes>
        <Route path="/register" element={<SignUp />}></Route>
        <Route path="/Login" element={<Login />}></Route>
        <Route path="/Home" element={<Home />}></Route>
      </Routes>
    </div>
  );
}
