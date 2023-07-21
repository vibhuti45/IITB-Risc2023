-- Importing the std_logic library
library ieee;
use ieee.numeric_std.all;
use ieee.std_logic_1164.all;
use ieee.std_logic_UNSIGNED.all;

entity alu is
    port(
        -- ALU input
        alu_a: in std_logic_vector(15 downto 0);
        alu_b: in std_logic_vector(15 downto 0);
        -- alu_e: in std_logic_vector(15 downto 0);
        
        -- e_en   : in std_logic;
        -- ALU output
        alu_c: out std_logic_vector(15 downto 0);

        -- To select alu operation
        alu_ir: in std_logic_vector(0 downto 0);

        -- Carry
        carry_out : out std_logic
  
    );
end entity alu ;

architecture working of alu is
    
begin
    alu_process:process(alu_a,alu_b,alu_ir)
    begin
        if(alu_ir = "0") then
            alu_c <= alu_a + alu_b;
            if (to_integer(unsigned(alu_a)) + to_integer(unsigned(alu_b))) > 65535 then
                carry_out <= '1';
            else
                carry_out <= '0';
            end if;
        else
				alu_c <= alu_a nand alu_b;
            carry_out <= '1';
        end if;
    end process alu_process;
end architecture working;