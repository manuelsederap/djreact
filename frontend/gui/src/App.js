import BaseRouter from './routes';
import { BrowserRouter as Router } from 'react-router-dom';
import './App.css';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import ArticleList from './containers/ArticleListView';

function App() {
  return (
    <div className="App">
      <Router>
        <CustomLayout>
          <BaseRouter />
        </CustomLayout>
      </Router>
    </div>
  );
}

export default App;
