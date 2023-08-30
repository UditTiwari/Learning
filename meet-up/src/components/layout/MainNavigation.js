import {Link} from 'react-router-dom';
import { useContext } from 'react';
import FavoritesContext from '../../store/favorites-context';
import classess from './MainNavigation.module.css'

function MainNavigatin(){
    const favoritesCtx = useContext(FavoritesContext);

    return (
         <header className={classess.header}>
            <div className={classess.logo}>Meetups App</div>
            <nav>
                <ul>
                    <li>
                        <Link to='/'>All Meetups</Link>
                    </li>
                    <li>
                        <Link to='/new-meetup'>Add New Meetups</Link>
                    </li>
                    <li>
                        <Link to='/favorites'>
                            My Favorites
                            <span className={classess.badge}>{favoritesCtx.totalFavorites}</span>
                            </Link>
                    </li>
                </ul>
            </nav>


        </header> 
    );
}


export default MainNavigatin;