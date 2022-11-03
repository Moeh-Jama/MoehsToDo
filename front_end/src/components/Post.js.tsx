import { 
  Card,
  CardContent,
} from "@mui/material";
import Typography from '@mui/material/Typography';
import React from "react";

export interface PostData {
  post_id: string;
  owner_id: string;
  content: string;
}

export const Post = ({post_id, owner_id, content} : PostData) => {
  return <Card>
    <CardContent>
      <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
        Post ID: {post_id}
      </Typography>
      <Typography variant="h5" component="div">
        
      </Typography>
      <Typography sx={{ mb: 1.5 }} color="text.secondary">
        Owner: {owner_id}
      </Typography>
      <Typography variant="body2">
        {content}
      </Typography>
    </CardContent>
  </Card>
}