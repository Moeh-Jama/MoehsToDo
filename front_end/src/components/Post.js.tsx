import { 
  Card,
  CardContent,
  Avatar,
} from "@mui/material";
import Typography from '@mui/material/Typography';
import React from "react";

export interface PostData {
  owner_id: string;
  firstname: string;
  profileImage: string;
  post_id: string;
  content: string;
}

export const Post = ( post : any ) => {
  console.log('cool hidden post', post);
  return <Card>
    <CardContent>
      <Avatar alt={post.post.firstname} src={post.post.profileImage} />
      <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
        Post ID: {post.post.post_id}
      </Typography>
      <Typography variant="h5" component="div">
      </Typography>
      <Typography sx={{ mb: 1.5 }} color="text.secondary">
        Owner: {post.post.owner_id}
      </Typography>
      <Typography variant="body2">
        {post.post.content}
      </Typography>
    </CardContent>
  </Card>
}