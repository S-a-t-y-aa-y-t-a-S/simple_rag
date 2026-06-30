import React, { useState, useEffect } from 'react'
import { LoaderCircle } from 'lucide-react'

const CustomComponent = ({flag}) => {

    if (flag === 0) {
        return (<span>
            Please upload a document
        </span>)
    }
    else if (flag == 1) {
        return (
            <span>
                testing ground for ingestion
            </span>
        )
    }
    else if (flag === 2) {
        return (
            <div className='flex gap-5'>
                <LoaderCircle className='animate-spin'/>
                Document is being ingested. Please wait!!
            </div>
        ) 
    }
    else if (flag === 3) {
        return (<span>
            Ingestion phase is complete!!
        </span>)
    }
    return null
}

const Playground = ({flag}) => {

    return (
        <div className='mt-50 flex justify-center font-bold tracking-wide text-gray-500'>
            {<CustomComponent flag={flag} />}
        </div>
    )
}

export default Playground