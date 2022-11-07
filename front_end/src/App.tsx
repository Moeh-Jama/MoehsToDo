import * as React from 'react';
import { SignUpForm } from './components/SignUpForm.js';
import { UserPosts } from './components/UserPosts.js';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Layout } from './components/Layout.js';
import { NavBarMenu } from './components/Navbar.js';
import axios from 'axios';
import { useEffect } from 'react';

export const App = () => {
  const [owner_id, setOwnerId] = React.useState("");

  const getCurrentuser = async() => {
    console.log('running axios');
    await axios.get(`http://127.0.0.1:5000/current_user/`)
      .then(res => {
        if (res.data['error'] !== undefined) {
          const ownerIdResult = res.data.owner_id;
          setOwnerId(ownerIdResult);
        } else {
          setOwnerId("be7b5a832d6843859383c78a53d91347");
        }
      });
  }

  useEffect(() => {
    owner_id == "" ? getCurrentuser(): null;
  }, [owner_id]);

  return <div>
    <NavBarMenu ownerId={owner_id}/>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="signup" element={<SignUpForm  setOwnerFunc={setOwnerId} />} />
          {owner_id == "" ? <></> : <Route path="posts" element={<UserPosts ownerId={owner_id} />} /> }
        </Route>
      </Routes>
    </BrowserRouter>
  </div>
};
