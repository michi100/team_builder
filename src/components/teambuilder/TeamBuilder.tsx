import "./teambuilder.css";
import { Board } from "../board/Board";
import { Synergy } from "../synergy/Synergy";
import { UnitList } from "../unitlist/UnitList";

export const TeamBuilder = () => {
  return (
    <div className="TeamBuilder">
      TeamBuilder
      <div className="GameView">
        GameView
        <Synergy />
        <Board />
      </div>
      <UnitList />
    </div>
  );
};
