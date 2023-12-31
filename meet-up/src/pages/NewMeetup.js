import { useHistory } from 'react-router-dom';

import NewMeetupForm from "../components/meetups/NewMeetupForm";

function NewmeetupPage(){
    const history = useHistory();

    function addMeetupHandler(meetupData){
        fetch
        (
                'https://meetup-app-3f1f4-default-rtdb.firebaseio.com/meetups.json',
            {
                method: 'POST',
                body: JSON.stringify(meetupData),
                headers:{
                    'Content-Type': 'application/json'
                }
            }
        ).then(() => {
            history.replace('/');
        });
    }

    return(
        <section>
            <h1>Add New Meetup</h1>
            {/* onAddMeetup  getting from another component */}
            <NewMeetupForm onAddMeetup={addMeetupHandler} />  

            </section>
    );

}


export default NewmeetupPage;