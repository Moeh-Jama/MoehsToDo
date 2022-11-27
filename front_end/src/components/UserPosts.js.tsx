// import { MissingParameter } from "./commons/MissingParameter";
import { SignalWifiStatusbarNullOutlined } from "@mui/icons-material";
import { Paper, Stack, styled } from "@mui/material";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Post, PostData } from "./Post.js"
export interface ownerProfile {
  ownerId: string;
};

interface rawPost {
  owner_id: string;
  content: string;
  post_id: string;
}

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));



export const UserPosts = (props:ownerProfile) => {
  const [userDetails, setUserDetails] = useState({ firstname: '', profile_image: ''});
  const [rawpostList, setRawPostList] = useState([]);
  const [postList, setPostList] = useState([]);

  const getUserPosts = () => {
    axios.get(`http://127.0.0.1:5000/post/${props.ownerId}`)
      .then(res => {
        const posts = res.data;
        console.log(posts.posts);
        setRawPostList(posts.posts);
      });
    
  };

  const getUserDetails = () => {
    axios.get(`http://127.0.0.1:5000/user/${props.ownerId}`)
      .then(res => {
        const user = res.data;
        setUserDetails(user.user);
      });
  };

  useEffect(() => {
    console.log(rawpostList.length);
    if (rawpostList.length == 0) {
      getUserPosts();
      getUserDetails();
    } else {
      const isPostsNotEmpty = Object.keys(rawpostList).length !== 0;
      const isUserNotEmpty = Object.keys(userDetails).length !== 0;
      console.log('is not empty?', isPostsNotEmpty, rawpostList.length);
      if (isPostsNotEmpty && isUserNotEmpty) {
        const posts = rawpostList.map((post: rawPost) => ({ ...post, username: userDetails.firstname, profileImage: userDetails.profile_image}));
        setPostList(posts)
      }
    }
  }, [rawpostList]);
 
  const posts = postList.map(( post: PostData ) => {
    console.log(post);
    return (
      <Item>
        <Post post={post}/>
      </Item>)
  });
  console.log('displaying posts', postList.length);
  return <Stack spacing={2}>{posts}</Stack>;
};