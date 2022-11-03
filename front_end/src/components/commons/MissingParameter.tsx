import { Alert } from "@mui/material";
import React from "react";

export const MissingParameter = (parameter: string) => (
  <Alert severity="warning">The paremeter {parameter} is necessary, please add it!</Alert>
)