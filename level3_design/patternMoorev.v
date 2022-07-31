module patternMoorev(
    input logic clk,
    input logic reset,
    input logic a,
    output logic y);

    parameter S0 = 3'b000;
    parameter S1 = 3'b001;
    parameter S2 = 3'b010;

    reg state, nextstate;
    // state register
    always @(posedge clk, posedge reset)
    begin
        if (reset) state <= S0;
        else state <= nextstate;
        // next state logic
        begin
            case (state)
            S0: if (a) nextstate = S0;
            else nextstate = S1;
            S1: if (a) nextstate = S2;
            else nextstate = S1;
            S2: if (a) nextstate = S0;
            else nextstate = S1;
            default: nextstate = S0;
            endcase
        end
    end
    // output logic
    always @(*)
    begin
        if(state == S2)
            assign y = 1;
    end
endmodule