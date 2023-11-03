import React, { useState } from 'react';

import './Difference.css'

export default function Difference() {
  const [number, setNumber] = useState('');
  const [data, setData] = useState([]);

  async function fetchDifference(number) {
    try {
      const response = await fetch(`http://localhost:8000/api/difference?number=${number}`);
      if (response.ok) {
        const result = await response.json();
        console.log(result)
        return result;
      } else {
        console.error('Error fetching data');
      }
    } catch (error) {
      console.error('Error fetching data', error);
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (number.trim() !== '') {
      const result = await fetchDifference(number);

      // convert to user friendly datetime
      const date = new Date(result.datetime);
      const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', timeZoneName: 'short' };
      const formattedDate = date.toLocaleDateString(undefined, options);

      setData([...data, {
        number: number,
        difference: result.difference,
        timestamp: formattedDate,
        occurrences: result.occurrences,
      }]);
    }
  };

  return (
    <div>
      <form className="Form" onSubmit={handleSubmit}>
        <label>
          Enter a number:
          <input type="text" value={number} onChange={(e) => setNumber(e.target.value)} />
        </label>
        <button type="submit">Submit</button>
      </form>
      <table className="Table">
        <thead>
          <tr>
            <th>Number</th>
            <th>Difference</th>
            <th>Requested at</th>
            <th>Occurrences</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.number}</td>
              <td>{item.difference}</td>
              <td>{item.timestamp}</td>
              <td>{item.occurrences}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
