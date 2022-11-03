import { ContentCopy } from "@mui/icons-material";
import React from "react";
import { ownerProfile } from "../UserPosts.js";

const copyTextToClipboard = (text: string) => {
  if ('clipboard' in navigator) {
    return navigator.clipboard.writeText(text);
  }
  return document.execCommand('copy', true, 'www');
}

export const ClickableCopyToClipboard = (ownerId: ownerProfile ) => {
  return <div onClick={() => copyTextToClipboard(ownerId.ownerId)}><ContentCopy/>
    </div>;
}