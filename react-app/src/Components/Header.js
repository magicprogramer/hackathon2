import { Link } from "react-router-dom";
import React from "react-router-dom";
export default function Header() {
  function handelLogOut() {
    window.localStorage.removeItem("email");
    window.location.reload();
    window.location.pathname = "/register";
  }

  return (
    <div className="container">
      <nav className="nav">
        <div>
          <Link className="another-links" to="/Home">
            <h4>Home</h4>
          </Link>
        </div>
        <div className="content">
          <div>
            {!window.localStorage.getItem("email") ? (
              <>
                {" "}
                <Link
                  to="/register"
                  style={{ textAlign: "center", marginRight: "15px" }}
                  className="register-nav "
                >
                  Register
                </Link>
                <Link
                  to="/Login"
                  style={{ textAlign: "center", margin: "4px" }}
                  className="register-nav"
                >
                  Login
                </Link>
              </>
            ) : (
              <div className="register-nav" onClick={handelLogOut}>
                Log Out
              </div>
            )}
          </div>
        </div>
      </nav>
    </div>
  );
}
