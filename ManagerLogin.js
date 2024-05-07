import React, { useRef, useState, useEffect, useContext } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "./context/AuthProvider";
import { Link } from "react-router-dom";
import axios from "./api/axios";
const LOGIN_URL = "/auth";

const ManagerLogin = () => {
    const { setAuth } = useContext(AuthContext);
    const emailInputRef = useRef();
    const passwordInputRef = useRef();
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [pwd, setPwd] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        emailInputRef.current.focus();
    }, []);

    useEffect(() => {
        setErrMsg("");
    }, [email, pwd]);

    const handleSubmit = async (e) => {
        e.preventDefault(); 
        try {
            const response = await axios.post(LOGIN_URL,
                JSON.stringify({email, pwd }),
                {
                    headers: {
                        "Content-Type": "application/json",
                    },
                    withCredentials: true,
                }
            );
            console.log(JSON.stringify(response?.data));
            const accessToken = response?.data?.accessToken;
            const roles = response?.data?.roles;
            setAuth({email, pwd, roles, accessToken });
            setEmail("");
            setPwd("");
            setSuccess(true);    
            navigate("/Dashboard");

        } catch (err) {
            if (!err.response) {
                setErrMsg("No server response");
            } else if (err.response.status === 401) {
                setErrMsg("Invalid credentials");
            } else if (err.response.status === 400) {
                setErrMsg("Missing credentials");
            } else {
                setErrMsg("Login failed. Please try again.");
            }
            if (email === "") {
                emailInputRef.current.focus();
            } else {
                passwordInputRef.current.focus();
            }
        }
    }

    return (
        <>  
            {success ? (
                <section>
                    <h1>Sign In Successful</h1>
                    <br />
                    <p>
                        <a href="#">Go to home</a>
                    </p>
                </section>
            ) : (
                <section>
                    <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    <h1 className="header">Restaurant's Management</h1>
                    <br/>
                    <div className="title">
                        <h2>Manager Login</h2>
                        <br />
                        <form className="content" onSubmit={handleSubmit}>
                            <label htmlFor="email"> E-mail: </label> 
                            <input
                                type="text"
                                id="email"
                                autoComplete="off"
                                onChange={(e) => setEmail(e.target.value)}
                                value={email}
                                required
                                ref={emailInputRef}
                            />
                            <br />
                            <br />
                            <label htmlFor="password"> Password: </label>
                            <input
                                type="password"
                                id="password"
                                onChange={(e) => setPwd(e.target.value)}
                                value={pwd}
                                required
                                ref={passwordInputRef}
                            />
                            <br />
                            <br />
                            <button className="button" type="submit">Login</button> 
                            <p>
                                Don't have an account?<br />
                                <button><Link to="/ManagerRegister">Sign up</Link></button>          
                            </p>
                        </form>
                    </div>    
                </section>
            )}
        </>
    );
}

export default ManagerLogin;
