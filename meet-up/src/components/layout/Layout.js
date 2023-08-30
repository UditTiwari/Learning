import classes from './Layout.module.css';
import MainNavigatin from './MainNavigation';

function Layout(props){

    return (
        <div>
            <MainNavigatin />
            <main className={classes.main}>{props.children}</main>
        </div>
    );
}

export default Layout;