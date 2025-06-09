import { useEffect, useState } from "react";
import { useNavigate, Link } from "react-router-dom";

function NotFound() {
  const navigate = useNavigate();
  const [countdown, setCountdown] = useState(10);

  useEffect(() => {
    const interval = setInterval(() => {
      setCountdown((prev) => prev - 1);
    }, 1000);

    const timeout = setTimeout(() => {
      navigate("/");
    }, 10000);

    return () => {
      clearInterval(interval);
      clearTimeout(timeout);
    };
  }, [navigate]);

  return (
    <div>
      <h2>404 Not Found</h2>
      <p>I am sorry, that location does not exist 😭</p>
      <p>
        <strong>You will be redirected to the home page in {countdown}...</strong>
      </p>
      <p>Or you can always <Link to="/">go home!</Link></p>
    </div>
  );
}

export default NotFound;
