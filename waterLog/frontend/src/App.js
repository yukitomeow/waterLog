import React from 'react';
import WaterConsumption from './WaterConsumption';

function App() {
    const username = 'SampleUser';  // You can fetch these values from an API or other sources
    const date = 'Today';
    const totalWaterToday = 500;   // Example value, replace with actual data

    return (
        <div className="App">
            <WaterConsumption 
                username={username} 
                date={date} 
                totalWaterToday={totalWaterToday} 
            />
            {/* Other components or HTML can go here */}
        </div>
    );
}

export default App;
