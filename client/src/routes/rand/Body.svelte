<script>
  import { randData } from "../../api/api.js";
  import Button from '../../components/UI/Button.svelte'

  import Input from '../../components/UI/Input.svelte'
  // export let view;
  // $: console.log('queryRand', view)
  let numberInput = 10;
  let data=randData(numberInput);

  import { createEventDispatcher } from 'svelte';
  
  const dispatch = createEventDispatcher()
  function submitForm() {
    data = randData(numberInput);
    console.log('submitForm', numberInput, data);
    dispatch('inputForm', 
    {numberInput:numberInput}
    )
    }
</script>

<style>

</style>

<h2>Random Number</h2>
<form on:submit|preventDefault={submitForm}>
  <Input 
  type= "text" 
  id="numberInput" 
  label="Enter a Number"
  value={numberInput} 
  on:input={event => (numberInput = event.target.value)}/>
</form>

<!-- <Button mode= "success" type= "button" on:click={submitForm}>Submits</Button> -->

{#await randData(numberInput)}
  <p>waiting</p>
{:then data}
  <p>Added your number to a random number using a Flask Python server and visualized with a Svelte front end: 
  <p>{data.params} + {data.randomNumber} = {data.sumRandomParams}</p>
{/await}
  
  