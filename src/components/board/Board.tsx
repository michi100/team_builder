import "./Board.css";
import { BoardGrid } from "./BoardGrid";

export const Board = () => {
  return (
    <div className="Board">
      Board
      <BoardGrid />
      <BoardGrid />
      <BoardGrid />
      <BoardGrid />
      <BoardGrid />
      <BoardGrid />
      <BoardGrid />
    </div>
  );
};
