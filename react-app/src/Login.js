import { useState } from "react";
import axios from "axios";
import Header from "./Components/Header";
export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [accept, setAccept] = useState(false);
  const [forEmail, setForEmail] = useState("");

  async function submit(ele) {
    let flag = true;
    ele.preventDefault();
    setAccept(true);
    try {
      if (flag) {
        const res = await axios.post("", {
          email: email,
          password: password,
        });
        if (res.status === 200) {
          window.localStorage.setItem("email", email);
          window.location.pathname = "/Home";
        }
      }
    } catch (err) {
      setForEmail(err.response.status);
    }
  }

  return (
    <div>
      <Header />
      <div className="parent">
        <div className="register">
          <form onSubmit={submit}>
            <label htmlFor="Eamil">Email:</label>
            <input
              required
              value={email}
              type="email"
              id="Email"
              placeholder="Email..."
              onChange={(e) => setEmail(e.target.value)}
            />
            {accept && forEmail === 422 && (
              <p className="error">Email Is Already Used</p>
            )}
            <label htmlFor="Password">Password:</label>
            <input
              value={password}
              type="Password"
              placeholder="Password"
              id="Password"
              onChange={(e) => setPassword(e.target.value)}
            />
            {password.length < 8 && accept && (
              <p className="error">Password Must Be More than 8 Chars</p>
            )}
            <div style={{ textAlign: "center" }}>
              <button type="submit">Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
