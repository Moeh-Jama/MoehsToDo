import { 
  FormControl,
  InputLabel,
  Input,
  FormHelperText,
  Button,
  Alert,
} from '@mui/material';
// import ContentPasteIcon from '@mui/icons-material/ContentPaste';
import React, { useState } from 'react';
import axios from 'axios';

export const SignUpForm = () => {
  const [firstname, setFirstname] = useState("");
  const [owner_id, setOwnerId] = useState("");
  const submitUserAccount = () => {
    console.log('running axios');
    axios.post(`http://127.0.0.1:5000/create_user/${firstname}`)
      .then(res => {
        const ownerIdResult = res.data.owner_id;
        setOwnerId(ownerIdResult);
      });
  }
  // ask to signup first time
  // else ask to login (small login button)
  return <div>
            {owner_id != "" ?  
              (<Alert severity="success">
                You Have successfully signed up: Your unique Id is {owner_id}
                </Alert>)
            : null}
            <FormControl>
              <InputLabel htmlFor="my-input">You Firstname</InputLabel>
              <Input id="my-input" aria-describedby="my-helper-text" onChange={e => setFirstname(e.target.value)}/>
              <FormHelperText id="my-helper-text">You can put in a nickname if you don't feel comfortable 😉</FormHelperText>
              <Button variant="outlined" onClick={() => submitUserAccount()}>Submit!</Button>
            </FormControl>
        </div>
}
