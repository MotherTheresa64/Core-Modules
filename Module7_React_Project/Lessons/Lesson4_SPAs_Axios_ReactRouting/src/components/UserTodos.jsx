import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

function UserTodos() {
  const { userId } = useParams();
  const [todos, setTodos] = useState([]);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUserAndTodos = async () => {
      try {
        const userRes = await axios.get(
          `https://jsonplaceholder.typicode.com/users/${userId}`
        );
        setUser(userRes.data);

        const todosRes = await axios.get(
          `https://jsonplaceholder.typicode.com/users/${userId}/todos`
        );
        setTodos(todosRes.data);
      } catch (err) {
        setError(`Failed to fetch: ${err.message}`);
      } finally {
        setLoading(false);
      }
    };

    if (userId) {
      fetchUserAndTodos();
    }
  }, [userId]);

  if (loading) return <p>Loading User Todos...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h2>Todos for: {user.name}</h2>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <p>
              <strong>Title:</strong> {todo.title}
            </p>
            <p>
              <strong>Completed:</strong> {todo.completed ? "✅" : "❌"}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserTodos;
