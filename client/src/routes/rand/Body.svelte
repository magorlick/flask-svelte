<script>
  import { randData } from "../../api/api.js";
  import Input from '../../components/UI/Input.svelte'
  let numberInput = 10;
  let data=randData(numberInput);

  function submitForm() {
    data = randData(numberInput);
    console.log('submitForm', numberInput, data);
    dispatch('inputForm', 
    {numberInput:numberInput}
    )
    }
</script>

<h2>This input (Svelte) is sent to a dynamic server and added to a random number (Python & Flask):</h2>
<form on:submit|preventDefault={submitForm}>
  <Input 
  type= "text" 
  id="numberInput" 
  label="Enter a Number"
  value={numberInput} 
  on:input={event => (numberInput = event.target.value)}/>
</form>

{#await randData(numberInput)}
  <p>Waiting for a response from Flask...</p>
{:then data}
  <p>Dynamically generated results: 
  <p>{data.params} + {data.randomNumber} = {data.sumRandomParams}</p>
{/await}
  
  