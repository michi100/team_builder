import { championImageList } from "../../assets";
import "./unitlist.css";
// import { Square } from "@mui/icons-material";

export const UnitList = () => {
  return (
    <>
      <div className="UnitList">
        UnitList
        {championImageList.map((src: string) => (
          <img src={src} style={{ width: "100px", height: "auto" }} />
        ))}
        {/* <Square /> */}
      </div>
    </>
  );
};
