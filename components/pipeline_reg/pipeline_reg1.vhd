library ieee; -- importing ieee library
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity pipeline_reg1 is
    port(
        -- inputs
        p1_ir_in: in std_logic_vector(15 downto 0);
        p1_pc_in: in std_logic_vector(15 downto 0) ;
        -- p1_opcode_in:in std_logic_vector(3 downto 0);
        -- p1_complement_in:in std_logic;
        -- p1_cz_in: in std_logic_vector(1 downto 0);
        
        -- outputs
        p1_ir_out: out std_logic_vector(15 downto 0);
        p1_pc_out: out std_logic_vector(15 downto 0) ;
        -- p1_opcode_out:out std_logic_vector(3 downto 0);
        -- p1_complement_out:out std_logic;
        -- p1_cz_out: out std_logic_vector(1 downto 0);

        -- enable
        p1_en   : in std_logic;
        -- clock
        clock   : in std_logic

    );
end entity pipeline_reg1;

architecture working of pipeline_reg1 is
    
begin
    p1_write_process:process(clock)
    begin
        if (falling_edge(clock)) then
            if (p1_en = '1') then
                p1_ir_out <= p1_ir_in;
                p1_pc_out <= p1_pc_in;
            end if;
        end if;
    end process p1_write_process;
end architecture working;