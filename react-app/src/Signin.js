import { useEffect, useState } from "react";
import axios from "axios";
import Header from "./Components/Header";

export default function SignUp(props) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [accept, setAccept] = useState(false);
  const [forEmail, setForEmail] = useState("");

  useEffect(() => {
    setName(props.name);
    setEmail(props.email);
  }, [props.name, props.email]);

  // async function submit(ele) {
  //   let flag = true;
  //   ele.preventDefault();
  //   setAccept(true);
  //   if (name === "" || password.length < 8) {
  //     flag = false;
  //   } else flag = true;
  //   try {
  //     if (flag) {
  //       let res = await axios.post(`api${props.lastWord}`, {
  //         name: name,
  //         email: email,
  //         password: password,
  //       });
  //       if (res.status === 200) {
  //         props.hasLocalStorage && window.localStorage.setItem("email", email);
  //         window.location.pathname = `/Home`;
  //       }
  //     }
  //   } catch (err) {
  //     console.log("Error:: ", err.response.data);
  //     setForEmail(err.response.data);
  //   }
  // }
  return (
    <div>
      <Header />
      <div className="register">
        <form onSubmit={"submit"}>
          <label htmlFor="Name">Name:</label>
          <input
            value={name}
            type="name"
            id="Name"
            placeholder="Name..."
            onChange={(e) => setName(e.target.value)}
          />
          {name === "" && accept && (
            <p className="error">Username Is Requied</p>
          )}
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
            type="password"
            placeholder="Password"
            id="Password"
            onChange={(e) => setPassword(e.target.value)}
          />
          {password.length < 8 && accept && (
            <p className="error">Password Must Be More than 8 Chars</p>
          )}
          <div style={{ textAlign: "center" }}>
            <button type="submit">Register</button>
          </div>
        </form>
      </div>
    </div>
  );
}
