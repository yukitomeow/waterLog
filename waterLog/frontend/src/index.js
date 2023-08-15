import React from 'react';
import ReactDOM from 'react-dom';
import WaterConsumption from './WaterConsumption';

ReactDOM.render(
    <WaterConsumption 
        username="{{ username }}"
        date="{{ date }}"
        totalWaterToday="{{ total_water_today }}"
    />,
    document.getElementById("react-root")
  );
  



