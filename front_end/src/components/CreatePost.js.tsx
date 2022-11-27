import { Button, FormControl, TextField } from "@mui/material";
import axios from "axios";
import React, { useState } from "react";

interface PostProps {
  ownerId: string
}
export const CreatePost = (props: PostProps) => {
  const [postMessage, setPostMessage] = useState("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPostMessage(event.target.value);
  }
  const saveComment = () => {
    const post = {
      ownerId: props.ownerId,
      postMessage: postMessage
    };

    axios({
      method: "POST",
      headers: {
        'Access-Control-Allow-Origin': true,
      },
      url: `http://127.0.0.1:5000/postee/${props.ownerId}`,
      data: post
    }).then((res) => console.log(res.data));
    console.log('content', post);
  };

  const pushPost = () => {
  };


  return <FormControl variant="standard" fullWidth>
  <TextField 
    id="new-comment" 
    label="Comment"
    multiline
    minRows={3}
    maxRows={5}
    // focused
    // autoFocus
    value={postMessage} 
    onChange={handleChange}
    // onKeyDown={keyPress}
  />
  <Button onClick={() => saveComment()}>
    Comment
  </Button>
</FormControl>

};