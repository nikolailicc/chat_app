import { PrettyChatWindow } from 'react-chat-engine-pretty';

const ChatsPage = (props) => {
  return (
    <div style={{ height: '100vh', width: '100vw' }}>
      <PrettyChatWindow
        projectId="5a8c4d08-6d5d-41a3-8ebe-049910b9fd7f"
        username={props.user.username}
        secret={props.user.secret}
        style={{ height: '100%' }}
      />
    </div>
  );
};

export default ChatsPage;
