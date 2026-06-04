import React from 'react'
import amazon from '/home/satyasish/Documents/react_tut/04-cards-project/src/assets/amazon.png'
import google from '/home/satyasish/Documents/react_tut/04-cards-project/src/assets/google_logo.jpeg'
import dribble from '/home/satyasish/Documents/react_tut/04-cards-project/src/assets/dribble_logo.png'
import figma from '/home/satyasish/Documents/react_tut/04-cards-project/src/assets/figma_logo.png'
import airbnb from '/home/satyasish/Documents/react_tut/04-cards-project/src/assets/airbnb_logo.png'
import apple from '/home/satyasish/Documents/react_tut/04-cards-project/src/assets/apple_logo.png'
import Cards from './components/Cards'



const App = () => {
  const list_of_jobs = [
    {
      logo: amazon,
      name: "Amazon",
      published: 5,
      designation: "Senior UI/UX",
      time: "Part-time",
      level: "Senior level",
      payment: "$120/hr", 
      place: "Mumbai"
    },
    {
      logo: google,
      name: "Google",
      published: 30,
      designation: "Graphics",
      time: "Part-time",
      level: "Flexible Schedule",
      payment: "$150-220k", 
      place: "Kochi"
    },
    {
      logo: dribble,
      name: "Dribble",
      published: 18,
      designation: "Senior Motion",
      time: "Contract",
      level: "Remote",
      payment: "$85/hr", 
      place: "Chennai"
    },
    {
      logo: figma,
      name: "Figma",
      published: 10,
      designation: "UX",
      time: "Full-time",
      level: "In office",
      payment: "$200-250k", 
      place: "Bangalore"
    },
    {
      logo: airbnb,
      name: "Airbnb",
      published: 5,
      designation: "Junior UI/UX",
      time: "Contract",
      level: "Remote",
      payment: "$100/hr", 
      place: "Delhi"
    },
    {
      logo: apple,
      name: "Apple",
      published: 5,
      designation: "Graphic",
      time: "Ful-Time",
      level: "Flexible Schedule",
      payment: "$85-120k", 
      place: "Noida"
    }
  ];

  return (
    <div className='parent'>
      {
        list_of_jobs.map((job)=> (
          <Cards 
            logo={job.logo} 
            name={job.name} 
            published={job.published} 
            designation={job.designation} 
            time={job.time} 
            level={job.level} 
            payment={job.payment} 
            place={job.place}
          />
      ))}
    </div>
  )
}

export default App