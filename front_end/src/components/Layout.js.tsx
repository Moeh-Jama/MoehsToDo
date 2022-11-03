import { Outlet, Link } from "react-router-dom";
import React from 'react';

export const Layout = () => {
    return <>
      <nav>
        <ul>
          <li>
            <Link to="/">Surprise Welcome</Link>
          </li>
          <li>
            <Link to="/signup">Signup</Link>
          </li>
          <li>
            <Link to="/posts">Posts</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
};
