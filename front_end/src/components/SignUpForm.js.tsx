import { 
  FormControl,
  InputLabel,
  Input,
  FormHelperText,
  Button,
  Alert,
} from '@mui/material';
// import ContentPasteIcon from '@mui/icons-material/ContentPaste';
import React, { Dispatch, SetStateAction, useState } from 'react';
import axios from 'axios';

interface IProps {
  setOwnerFunc: Dispatch<SetStateAction<string>>;
}

export const SignUpForm = (props: IProps
  ) => {
  const [firstname, setFirstname] = useState("");
  const [profileImage, setProfileImage] = useState("");
  const [owner_id, setOwnerId] = useState("");
  const submitUserAccount = () => {
    const postData = {
      firstName: firstname,
      profileImage: profileImage
    }
    axios({
      method: "POST",
      headers: {
        'Access-Control-Allow-Origin': true,
      },
      url: `http://127.0.0.1:5000/create_user/${firstname}`,
      data: postData
    }).then((res) => {
      const ownerIdResult = res.data.owner_id;
      setOwnerId(ownerIdResult);
      props.setOwnerFunc(ownerIdResult)
    });
  }

  // ask to signup first time
  // else ask to login (small login button) profileImage
  return <div>
            {owner_id != "" ?  
              (<Alert severity="success">
                You Have successfully signed up: Your unique Id is {owner_id}
                </Alert>)
            : null}
            <FormControl>
            <InputLabel htmlFor="my-input-profile">User Image url (OPTIONAL)</InputLabel>
              <Input id="my-input-profile" aria-describedby="my-helper-text-profile" onChange={e => setProfileImage(e.target.value)}/>
              <InputLabel htmlFor="my-input-name">You Firstname</InputLabel>
              <Input id="my-input-name" aria-describedby="my-helper-text-name" onChange={e => setFirstname(e.target.value)}/>
              <FormHelperText id="my-helper-text-name">You can put in a nickname if you don't feel comfortable 😉</FormHelperText>
              <Button variant="outlined" onClick={() => submitUserAccount()}>Submit!</Button>
            </FormControl>
        </div>
}
