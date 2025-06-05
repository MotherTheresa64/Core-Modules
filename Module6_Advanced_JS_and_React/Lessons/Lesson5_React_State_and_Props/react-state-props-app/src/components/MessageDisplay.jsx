function MessageDisplay({ message = "Props help us communicate between components." }) {
  return (
    <div className="message-display">
      <h3>Message:</h3>
      <p>{message}</p>
    </div>
  );
}

export default MessageDisplay;
