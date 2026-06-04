import React from "react";
import LeftUpper from "./LeftUpper";
import LeftLower from "./LeftLower";

const LeftContent = () => {
  //  bg-blue-300
  return (
    <div className="h-full w-1/3 shrink-0 flex flex-col justify-between">
      <LeftUpper />
      <LeftLower />
    </div>
  );
};

export default LeftContent;
