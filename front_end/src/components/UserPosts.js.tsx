// import { MissingParameter } from "./commons/MissingParameter";
import { Paper, Stack, styled } from "@mui/material";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Post } from "./Post.js"
export interface ownerProfile {
  ownerId: string;
};

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

export const UserPosts = (props:ownerProfile) => {
  const [postList, setPostList] = useState([]);
  const getUserPosts = () => {
    axios.get(`http://127.0.0.1:5000/post/${props.ownerId}`)
      .then(res => {
        const posts = res.data;
        setPostList(posts.posts);
      });
  }

  useEffect(() => {
    postList.length == 0 ? getUserPosts(): null;
  }, [postList]);
  const posts = postList.map(post => {
    return (
      <Item>
        <Post owner_id={post.owner_id} post_id={post.post_id} content={post.content}/>
      </Item>)
  })
  return <Stack spacing={2}>{posts}</Stack>;
};