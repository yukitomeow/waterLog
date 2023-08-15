import React, { useState } from 'react';

function WaterConsumption(props) {
    const [unit, setUnit] = useState('ml'); // Default to ml
    const consumptionInMl = props.totalWaterToday; 
    const consumptionInOz = consumptionInMl * 0.033814; // Convert ml to oz

    return (
        <div>
            <h2>Water Consumption for Today</h2>
            <p><strong>Username:</strong> {props.username}</p>
            <p><strong>Date:</strong> {props.date}</p>
            <p><strong>Total Water Consumed Today:</strong> 
               {unit === 'ml' ? consumptionInMl : consumptionInOz.toFixed(2)} {unit}
            </p>
            <label>
                Choose unit: 
                <select value={unit} onChange={(e) => setUnit(e.target.value)}>
                    <option value="ml">ml</option>
                    <option value="oz">oz</option>
                </select>
            </label>
        </div>
    );
}

export default WaterConsumption;

