<script>
    export let type = null;
    export let id;
    export let value;
    // export let multivalue = [];
    export let label;

    export let valid = true;
    export let validityMessage = "";

    let touched = false;
    let multivalue = ['one', 'two', 'three'];
    let values = multivalue;
</script>

<style>
  input,
  textarea {
    display: block;
    width: 100%;
    font-family: "Ubuntu";
    font-size: 1rem;
    border: none;
    border-bottom: 2px solid #ccc;
    border-radius: 3px 3px 0 0;
    background: var(--color--brand-primary--100);
    padding: 0.15rem 0.25rem;
    transition: border-color 0.1s ease-out;
  }

  input:focus,
  textarea:focus {
    border-color: #017e3d;
    outline: none;
  }

  label {
    display: block;
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    width: 100%;
  }

  .form-control {
    padding: 0.5rem 0;
    padding-top: 0.75rem;
    width: 100%;
    margin: 0.25rem 0;

  }

  .invalid {
      border-color:darkred;
      border-color: var(--color--brand-accent--100);
  }
  .error-message {
      color:darkred;
      margin: 0.25rem 0;
  }
</style>

<div class="form-control">
    <label for="{id}">{label}</label>
    {#if type === "text"}
    <input class:invalid="{!valid && touched}" type="{type}" id="{id}" value={value} on:input on:blur={() => touched = true}>
    {:else if type === "date"}
    <input class:invalid="{!valid && touched}" type="{type}" id="{id}" value={value} on:input on:blur={() => touched = true}>
    {:else if type === "multiselect"}    
    <div>
      <select multiple name="{id}"  id="{id}" bind:value={values} on:input on:blur={() => touched = true}>
        {#each multivalue as value}
          <option value={value}>
            {value}
          </option>
          
        {/each}
      </select>
    </div>
    {/if}
    {#if validityMessage && !valid && touched}
        <p class="error-message">{validityMessage}</p>
    {/if}
</div>