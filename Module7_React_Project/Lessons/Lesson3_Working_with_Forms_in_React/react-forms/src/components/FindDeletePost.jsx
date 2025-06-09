import { useState } from 'react';

function FindDeletePost() {
  const [postId, setPostId] = useState('');
  const [post, setPost] = useState(null);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handlePostIdChange = (event) => {
    setPostId(event.target.value);
  };

  const validateForm = () => {
    if (postId.trim() === '') {
      setError('Post ID is required');
      return false;
    }
    setError('');
    return true;
  };

  const findPost = async (event) => {
    event.preventDefault();

    if (!validateForm()) return;

    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`);

      if (!response.ok) {
        setPost('');
        throw new Error('Failed to find post');
      }

      const data = await response.json();
      setPost(data);
      setPostId(data.id);
    } catch (error) {
      setError(error.message);
    }
  };

  const deletePost = async () => {
    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`, {
        method: 'DELETE',
      });

      if (!response.ok) throw new Error('Failed to delete post');

      setSuccess(`Post #${postId} deleted successfully`);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <h1>Find a Post</h1>
      <form onSubmit={findPost}>
        <div>
          <label htmlFor="postId">Post ID:</label><br />
          <input
            type="number"
            id="postId"
            value={postId}
            onChange={handlePostIdChange}
            placeholder="Enter post ID"
          />
        </div><br />
        <button type="submit">Find Post</button>
      </form>

      {post && (
        <div>
          <p><b>Post Title:</b> {post.title}</p>
          <p><b>Post Body:</b> {post.body}</p>
          <button onClick={deletePost}>Delete Post</button>
        </div>
      )}

      {error && <div className="error">{error}</div>}
      {success && <div className="success">{success}</div>}
    </div>
  );
}

export default FindDeletePost;
