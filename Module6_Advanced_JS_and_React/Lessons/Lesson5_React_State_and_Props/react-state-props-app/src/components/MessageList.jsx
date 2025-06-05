function MessageList({ users }) {
  return (
    <div className="user-list">
      <h3>Usernames:</h3>
      <ul>
        {users.map((user, idx) => (
          <li key={idx}>{user}</li>
        ))}
      </ul>
    </div>
  );
}

export default MessageList;
