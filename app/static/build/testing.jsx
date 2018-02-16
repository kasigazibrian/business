const colorarray=[
    'red',
    'blue',
    'green',
    'orange',
    'purple',
    'cyan',
    'brown',
    'yellow',
    'lightblue'
];
class HelloWorld extends React.Component{
    constructor(props){
        super(props);

        this.state={
            color: 'hotpink'

        };

    }
    componentDidMount(){
        let colorPos= 0;
        setInterval(()=>{
            if (colorarray.length>colorPos){
                this.setState({
                    color: colorarray[colorPos]
                });
                colorPos++
            }
            else{
                this.setState({
                    color: colorarray[colorPos]
                });

                colorPos=0;
            }

        },1000);
    }
    toggleColor(){
        if (this.state.color =='hotpink'){
            this.setState({
                color: 'blue'
            });
        }
        else{
            this.setState({
               color: 'hotpink'
            });
        }

    }
    colorChange(event){
        this.setState({
            color: event.target.value
        });
    }
    render(){
        const styleObj={
            background: this.state.color,
            fontSize: '50'
        };

        return(
            <div id='hello' style={styleObj}>
                <h2 onClick={this.toggleColor.bind(this)} >{this.state.color}</h2>
                <h3>{this.props.name}</h3>
                <input type='text' value={this.state.color} onChange={this.colorChange.bind(this)}/>

            </div>
        );
    }
}
ReactDOM.render(
    <HelloWorld name='Kasigazi'/> ,document.getElementById('view')
);