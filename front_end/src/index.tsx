import * as React from 'react';
import {createRoot} from 'react-dom/client'
import { App } from './App';
const el = document.getElementById('root')
console.debug('we ran');
if (el === null) throw new Error('Root container missing in index.html')
const root = createRoot(el)
root.render(
  <App/>
);